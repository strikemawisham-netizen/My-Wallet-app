[app]
title = My Wallet App
package.name = mywalletapp
package.domain = com.strike.mywalletapp
source.dir =.
version = 0.1
requirements = python3,kivy==2.3.0
orientation = portrait

[buildozer]
log_level = 2

[app:android]
android.api = 33
android.minapi = 21
android.ndk = 25b
android.sdk = 33
android.accept_sdk_license_agreement = True
android.build_tools_version = 33.0.2
p4a.branch = master
