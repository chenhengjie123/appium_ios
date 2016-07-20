APP_NAME="appForUITest"

xcodebuild -target ${APP_NAME} -sdk iphoneos -configuration Debug
xcrun -sdk iphoneos PackageApplication -v build/Debug-iphoneos/${APP_NAME}.app -o /Users/hengjiechen/Documents/Training/appium_ios/app/AppForUITest/appForUITest/build/Debug-iphoneos/${APP_NAME}.ipa
