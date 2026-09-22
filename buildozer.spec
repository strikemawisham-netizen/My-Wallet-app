name: Build APK
on: [push]
jobs:
  build:
    runs-on: ubuntu-22.04
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-java@v4
        with:
          distribution: temurin
          java-version: '17'
      - uses: android-actions/setup-android@v3
      - uses: actions/setup-python@v5
        with:
          python-version: '3.10'
      - name: Install dependencies
        run: |
          sudo apt update
          sudo apt install -y zip unzip libncurses5-dev libffi-dev libssl-dev automake autoconf libtool pkg-config zlib1g-dev libltdl-dev
          pip install --upgrade pip
          pip install buildozer cython==0.29.33
      - name: Build APK
        run: |
          yes | buildozer android debug
      - name: Upload APK
        uses: actions/upload-artifact@v4
        with:
          name: my-wallet-apk
          path: bin/*.apk
android.api = 33
android.minapi = 21
android.ndk = 25b
android.sdk = 33
