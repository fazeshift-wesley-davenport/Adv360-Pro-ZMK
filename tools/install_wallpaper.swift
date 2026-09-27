import AppKit
import Foundation

func fail(_ message: String) -> Never {
    fputs("wallpaper-install: \(message)\n", stderr)
    exit(1)
}

let fileManager = FileManager.default
let imageURL: URL

if let path = CommandLine.arguments.dropFirst().first {
    imageURL = URL(fileURLWithPath: NSString(string: path).expandingTildeInPath).standardizedFileURL
} else {
    let pictures = fileManager.homeDirectoryForCurrentUser.appendingPathComponent("Pictures", isDirectory: true)
    let files = (try? fileManager.contentsOfDirectory(
        at: pictures,
        includingPropertiesForKeys: [.contentModificationDateKey],
        options: [.skipsHiddenFiles]
    )) ?? []
    let candidates = files.filter {
        $0.lastPathComponent.hasPrefix("adv360-layout-wallpaper-") && $0.pathExtension.lowercased() == "png"
    }
    guard let latest = candidates.max(by: { a, b in
        let aDate = (try? a.resourceValues(forKeys: [.contentModificationDateKey]).contentModificationDate) ?? .distantPast
        let bDate = (try? b.resourceValues(forKeys: [.contentModificationDateKey]).contentModificationDate) ?? .distantPast
        return aDate < bDate
    }) else {
        fail("no Adv360 wallpaper found in \(pictures.path); run tools/ops wallpaper first")
    }
    imageURL = latest.standardizedFileURL
}

guard fileManager.fileExists(atPath: imageURL.path), NSImage(contentsOf: imageURL) != nil else {
    fail("not a readable image: \(imageURL.path)")
}

let screens = NSScreen.screens
guard !screens.isEmpty else { fail("no displays found") }

let workspace = NSWorkspace.shared
for screen in screens {
    do {
        let options = workspace.desktopImageOptions(for: screen) ?? [:]
        try workspace.setDesktopImageURL(imageURL, for: screen, options: options)
    } catch {
        fail("could not set wallpaper on a display: \(error)")
    }
}

// The desktop service can take a moment to report the newly installed image.
let targetPath = imageURL.resolvingSymlinksInPath().path
var installed = false
for _ in 0..<20 {
    installed = screens.allSatisfy { screen in
        workspace.desktopImageURL(for: screen)?.resolvingSymlinksInPath().path == targetPath
    }
    if installed { break }
    RunLoop.current.run(until: Date().addingTimeInterval(0.1))
}
guard installed else { fail("desktop image did not update on every display") }

print("wallpaper-install: set \(imageURL.path) on \(screens.count) display(s)")
