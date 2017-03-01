TEMPLATE = aux

NAME=Sailfish_Keyboard_nl-arrows

OTHER_FILES = \
        layout/* \
        rpm/* \
        README.md

layout.files = layout/*
layout.path = /usr/share/maliit/plugins/com/jolla/layouts/

INSTALLS += \
        layout
