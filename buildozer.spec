[app]
title = My Wallet App
package.name = mywalletapp
package.domain = com.strike.mywalletapp
source.dir = .
version = 0.1
requirements = python3,kivy==2.3.0
orientation = portrait

# Android configuration mapping parameters
android.api = 33
android.minapi = 21
android.ndk = 25c
android.accept_sdk_license = True
android.archs = arm64-v8a

[buildozer]
log_level = 2
