[app]
title = My Wallet App
package.name = mywalletapp
package.domain = com.strike.mywalletapp
source.dir =.
version = 0.1
requirements = python3,kivy==2.3.1
orientation = portrait

[buildozer]
log_level = 2

[app:android]
android.api = 33
android.minapi = 21
android.accept_sdk_license_agreement = True
android.archs = arm64-v8a
