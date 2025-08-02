# 📦 MyLibrary – Minimal Xcode Dynamic Library Project via Python

This repository demonstrates how to scaffold a complete Xcode-compatible dynamic library project using a **single Python script**.

## 🧠 Why This Works

Xcode projects are just structured folders and text-based files (`.pbxproj`, `.plist`, source files, etc.). This script:

- **Generates the correct folder structure**
- **Creates valid C source/header files**
- **Creates a minimal `.xcodeproj/project.pbxproj`** with the required object entries
- Places files in expected paths so Xcode won't mark them red
- Ensures that the `.pbxproj` file includes:
  - Build configurations (Debug/Release)
  - Target setup (`PBXNativeTarget`)
  - File references and build phases
  - `PBXGroup` and `PBXSourcesBuildPhase` entries that mirror Xcode's expectations

## 📂 Structure Created

```
MyLibrary/
├── Info.plist
├── module.modulemap
├── MyLibrary.c
├── MyLibrary.h
├── Tests/
│   └── MyLibraryTests/
│       └── test_MyLibrary.c
└── MyLibrary.xcodeproj/
    └── project.pbxproj
```

## ⚙️ What the Python Script Does

- Defines the `structure` dictionary with all required paths and content
- Creates:
  - A header file `MyLibrary.h`
  - A source file `MyLibrary.c` with a simple `hello()` function
  - A test file `test_MyLibrary.c`
  - A module map for Clang module support
  - An `Info.plist` for metadata
- Generates a **fully-formed `.pbxproj`** file by manually writing the correct XML/plist structure including:
  - File references
  - Groups
  - Target and build phases
  - Debug/Release configs
- Writes all files to disk with correct paths using Python’s `os.makedirs` and `open()`

## 🧪 Try It

```bash
python is.py
open MyLibrary/MyLibrary.xcodeproj
```

Then press ⌘B in Xcode to build your dynamic library.

## ✅ Why the Files Show Up in Xcode

- Files are no longer red because:
  - The `.pbxproj` references paths like `MyLibrary.c`
  - And the script now places `MyLibrary.c` in the root of `MyLibrary/`, exactly where Xcode expects them
- The build phase correctly includes the `.c` file for compilation
- The header is included for completeness and optional `module.modulemap` exposure

## 🛠️ Extend This

- Add more `.c`/`.h` files
- Add static libraries or frameworks
- Extend `PBXBuildPhase` to include headers or resources
- Add Swift targets by adjusting `productType`

---

This setup gives you a working, buildable Xcode project without ever opening Xcode manually to configure it.
