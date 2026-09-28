[app]
title = My Wallet App
package.name = mywalletapp
package.domain = com.strike.mywalletapp
source.dir =.
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3,kivy==2.3.1
orientation = portrait

[buildozer]
log_level = 2
warn_on_root = 1

[app:android]
android.api = 33
android.minapi = 21
android.ndk = 25b
android.accept_sdk_license_agreement = True
android.archs = arm64-v8a
p4a.branch = master
