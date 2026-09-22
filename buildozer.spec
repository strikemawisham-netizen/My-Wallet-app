[app]
title = MinimalBuild
package.name = minimalbuild
package.domain = org.example

source.dir = .
source.include_exts = py,png,jpg,kv,atlas

version = 0.1
requirements = python3,kivy==2.3.0

orientation = portrait
fullscreen = 0

# Android specific configurations
android.api = 34
android.minapi = 21
android.ndk_api = 21
android.accept_sdk_license = True
android.skip_update = False

# Build restrictions
android.archs = arm64-v8a, armeabi-v7a
android.allow_backup = True

[buildozer]
log_level = 2
warn_on_root = 1
