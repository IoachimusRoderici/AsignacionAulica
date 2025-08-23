import QtQuick 2.15
import QtQuick.Window 2.15
import QtQuick.Controls 2.15
import QtQuick.Layouts 1.15

import "./BarraLateral"

Window {
    id: mainWindow
    visible: true
    visibility: Window.Maximized
    width: 800
    height: 600
    title: qsTr("Asignación Áulica")

    // Main layout with sidebar and content area
    RowLayout {
        anchors.fill: parent

        BarraLateral{
            id: sidebar
        }

        // Content area with loader
        Loader {
            id: tabLoader
            Layout.fillWidth: true
            Layout.fillHeight: true

            property string pestaña_actual: "Edificios"

            sourceComponent: {
                switch(pestaña_actual) {
                    case "Edificios": return homeComponent
                    case "Aulas": return profileComponent
                    case "Carreras": return settingsComponent
                    case "Materias": return messagesComponent
                    case "Horarios": return notificationsComponent
                    default: return homeComponent
                }
            }
        }
    }

    // Component definitions for different tab contents
    Component {
        id: homeComponent
        Rectangle {
            color: "white"
            Text {
                anchors.centerIn: parent
                text: "Home Content"
                font.pixelSize: 24
            }
        }
    }

    Component {
        id: profileComponent
        Rectangle {
            color: "lightblue"
            Text {
                anchors.centerIn: parent
                text: "Profile Content"
                font.pixelSize: 24
            }
        }
    }

    Component {
        id: settingsComponent
        Rectangle {
            color: "lightgreen"
            Text {
                anchors.centerIn: parent
                text: "Settings Content"
                font.pixelSize: 24
            }
        }
    }

    Component {
        id: messagesComponent
        Rectangle {
            color: "lightyellow"
            Text {
                anchors.centerIn: parent
                text: "Messages Content"
                font.pixelSize: 24
            }
        }
    }

    Component {
        id: notificationsComponent
        Rectangle {
            color: "lightpink"
            Text {
                anchors.centerIn: parent
                text: "Notifications Content"
                font.pixelSize: 24
            }
        }
    }
}
