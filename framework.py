import os

project_name = "MyLibrary"
src_dir = f"{project_name}"
tests_dir = f"{project_name}/Tests/{project_name}Tests"

structure = {
    src_dir: {
        f"{project_name}.h": f"""#ifndef {project_name.upper()}_H
#define {project_name.upper()}_H

void hello();

#endif /* {project_name.upper()}_H */
""",
        f"{project_name}.c": f"""#include "{project_name}.h"
#include <stdio.h>

void hello() {{
    printf("Hello from {project_name}!\\n");
}}
"""
    },
    tests_dir: {
        f"test_{project_name}.c": f"""#include "{project_name}.h"

int main() {{
    hello();
    return 0;
}}
"""
    },
    f"{project_name}/module.modulemap": f"""module {project_name} {{
    header "{project_name}.h"
    export *
}}""",
    f"{project_name}/Info.plist": """<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" \
"http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>CFBundleIdentifier</key>
    <string>com.example.mylibrary</string>
    <key>CFBundleName</key>
    <string>MyLibrary</string>
</dict>
</plist>"""
}

project_file_path = f"{project_name}/{project_name}.xcodeproj/project.pbxproj"
structure[project_file_path] = f"""// !$*UTF8*$!
{{
  archiveVersion = 1;
  classes = {{}};
  objectVersion = 55;
  objects = {{
    1D6058900D05DD3D006BFB54 /* Project object */ = {{
      isa = PBXProject;
      buildConfigurationList = 1D60589B0D05DD3E006BFB54 /* Build configuration list */;
      compatibilityVersion = "Xcode 3.2";
      mainGroup = 1D60588D0D05DD3D006BFB54;
      targets = (
        1D6058910D05DD3E006BFB54 /* {project_name} */,
      );
    }};

    1D60588D0D05DD3D006BFB54 = {{
      isa = PBXGroup;
      children = (
        FFFFFFFF0000000000000001 /* {project_name}.c */,
        FFFFFFFF0000000000000002 /* {project_name}.h */,
      );
      sourceTree = "<group>";
    }};

    1D6058910D05DD3E006BFB54 /* {project_name} */ = {{
      isa = PBXNativeTarget;
      name = {project_name};
      productName = {project_name};
      productType = "com.apple.product-type.framework";
      buildConfigurationList = 1D60589C0D05DD3E006BFB54;
      buildPhases = (
        FFFFFFFF0000000000000003 /* Sources */,
      );
      buildRules = ();
      dependencies = ();
    }};

    FFFFFFFF0000000000000001 /* {project_name}.c */ = {{
      isa = PBXFileReference;
      lastKnownFileType = sourcecode.c.c;
      path = {project_name}.c;
      sourceTree = "<group>";
    }};
    FFFFFFFF0000000000000002 /* {project_name}.h */ = {{
      isa = PBXFileReference;
      lastKnownFileType = sourcecode.c.h;
      path = {project_name}.h;
      sourceTree = "<group>";
    }};
    FFFFFFFF0000000000000003 /* Sources */ = {{
      isa = PBXSourcesBuildPhase;
      buildActionMask = 2147483647;
      files = (
        FFFFFFFF0000000000000004 /* {project_name}.c in Sources */,
      );
      runOnlyForDeploymentPostprocessing = 0;
    }};
    FFFFFFFF0000000000000004 /* {project_name}.c in Sources */ = {{
      isa = PBXBuildFile;
      fileRef = FFFFFFFF0000000000000001 /* {project_name}.c */;
    }};

    1D60589B0D05DD3E006BFB54 /* Build configuration list */ = {{
      isa = XCConfigurationList;
      buildConfigurations = (
        1D60589D0D05DD3E006BFB54 /* Debug */,
        1D60589E0D05DD3E006BFB54 /* Release */,
      );
      defaultConfigurationIsVisible = 0;
      defaultConfigurationName = Debug;
    }};
    1D60589D0D05DD3E006BFB54 /* Debug */ = {{
      isa = XCBuildConfiguration;
      name = Debug;
      buildSettings = {{
        PRODUCT_NAME = "$(TARGET_NAME)";
      }};
    }};
    1D60589E0D05DD3E006BFB54 /* Release */ = {{
      isa = XCBuildConfiguration;
      name = Release;
      buildSettings = {{
        PRODUCT_NAME = "$(TARGET_NAME)";
      }};
    }};

    1D60589C0D05DD3E006BFB54 = {{
      isa = XCConfigurationList;
      buildConfigurations = (
        1D60589D0D05DD3E006BFB54 /* Debug */,
        1D60589E0D05DD3E006BFB54 /* Release */,
      );
      defaultConfigurationIsVisible = 0;
      defaultConfigurationName = Debug;
    }};
    1D60589D0D05DD3E006BFB54 /* Debug */ = {{
      isa = XCBuildConfiguration;
      name = Debug;
      buildSettings = {{
        PRODUCT_NAME = "$(TARGET_NAME)";
      }};
    }};
    1D60589E0D05DD3E006BFB54 /* Release */ = {{
      isa = XCBuildConfiguration;
      name = Release;
      buildSettings = {{
        PRODUCT_NAME = "$(TARGET_NAME)";
      }};
    }};
  }};

  rootObject = 1D6058900D05DD3D006BFB54;
}}
"""

def scaffold(structure):
    for path, content in structure.items():
        if isinstance(content, dict):
            os.makedirs(path, exist_ok=True)
            scaffold({os.path.join(path, k): v for k, v in content.items()})
        else:
            os.makedirs(os.path.dirname(path), exist_ok=True)
            with open(path, "w") as f:
                f.write(content)

scaffold(structure)
print("✅ Framework project scaffolded.")
