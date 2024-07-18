PACKAGE=bgpython
BGBSPD_BUILD_DIR?=../bgbspd

WEB_IMAGES=$(wildcard src/*.png src/*.svg)

include $(BGBSPD_BUILD_DIR)/main.make
