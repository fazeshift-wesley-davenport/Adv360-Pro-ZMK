// Packs a light and a dark PNG into one HEIC that macOS switches with the system appearance.
// usage: swift tools/make_dynamic_heic.swift light.png dark.png out.heic
import AppKit
import Foundation
import ImageIO
import UniformTypeIdentifiers

func fail(_ message: String) -> Never {
    fputs("make-dynamic-heic: \(message)\n", stderr)
    exit(1)
}

let args = CommandLine.arguments.dropFirst().map { NSString(string: $0).expandingTildeInPath }
guard args.count == 3 else { fail("usage: make_dynamic_heic.swift light.png dark.png out.heic") }

func cgImage(_ path: String) -> CGImage {
    guard let source = CGImageSourceCreateWithURL(URL(fileURLWithPath: path) as CFURL, nil),
          let image = CGImageSourceCreateImageAtIndex(source, 0, nil) else { fail("cannot read \(path)") }
    return image
}

let light = cgImage(args[0])
let dark = cgImage(args[1])
let outURL = URL(fileURLWithPath: args[2])

// apple_desktop:apr holds a base64 binary plist naming the light (l) and dark (d) frame indexes.
let appearance = try PropertyListSerialization.data(fromPropertyList: ["l": 0, "d": 1], format: .binary, options: 0)
let metadata = CGImageMetadataCreateMutable()
let namespace = "http://ns.apple.com/namespace/1.0/" as CFString
guard CGImageMetadataRegisterNamespaceForPrefix(metadata, namespace, "apple_desktop" as CFString, nil),
      let tag = CGImageMetadataTagCreate(namespace, "apple_desktop" as CFString, "apr" as CFString, .string, appearance.base64EncodedString() as CFString),
      CGImageMetadataSetTagWithPath(metadata, nil, "apple_desktop:apr" as CFString, tag) else { fail("cannot build appearance metadata") }

guard let destination = CGImageDestinationCreateWithURL(outURL as CFURL, UTType.heic.identifier as CFString, 2, nil) else {
    fail("cannot create \(outURL.path)")
}
let options = [kCGImageDestinationLossyCompressionQuality: 0.9] as CFDictionary
CGImageDestinationAddImageAndMetadata(destination, light, metadata, options)
CGImageDestinationAddImage(destination, dark, options)
guard CGImageDestinationFinalize(destination) else { fail("cannot write \(outURL.path)") }
print("make-dynamic-heic: wrote \(outURL.path)")
