-- Shared build scripts from repo_build package.
repo_build = require("omni/repo/build")

-- Repo root
root = repo_build.get_abs_path(".")

-- Set the desired MSVC, WINSDK, and MSBUILD versions before executing the kit template premake configuration.
MSVC_VERSION = "14.27.29110"
WINSDK_VERSION = "10.0.18362.0"
MSBUILD_VERSION = "Current"

-- Execute the kit template premake configuration, which creates the solution, finds extensions, etc.
dofile("_repo/deps/repo_kit_tools/kit-template/premake5.lua")

-- Apps: for each app generate batch files and a project based on kit files (e.g. my_name.my_app.kit)
define_app("lp.omniscripts")

repo_build.prebuild_link {
    { "source/scripts", "_build/$platform/$config/scripts" },
    { "PACKAGE-LICENSES", "_build/PACKAGE-LICENSES" }
}

repo_build.prebuild_copy{"README.md", "_build/$platform/$config/README.md"}
repo_build.prebuild_copy{"link_app.sh", "_build/$platform/$config/link_app.sh"}

