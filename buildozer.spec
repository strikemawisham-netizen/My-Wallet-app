name: Build APK
on: [push]

jobs:
  build:
    runs-on: ubuntu-22.04
    steps:
      - name: Checkout Code
        uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.11'

      - name: Install System Dependencies
        run: |
          sudo apt-get update
          sudo apt-get install -y \
            build-essential \
            ccache \
            git \
            libffi-dev \
            libssl-dev \
            openjdk-17-jdk \
            unzip \
            zip \
            zlib1g-dev

      - name: Install Buildozer and Cython
        run: |
          pip install --upgrade pip
          pip install buildozer cython virtualenv

      - name: Build APK with Buildozer
        run: |
          # The NO_DOCKER=1 flag forces buildozer to run natively on the runner
          export NO_DOCKER=1
          buildozer android debug

      - name: Upload APK Artifact
        uses: actions/upload-artifact@v4
        with:
          name: apk-file
          path: bin/*.apk
          
