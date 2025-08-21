import QtQuick
import QtQuick.Window
import QtQuick.Controls
import QtQuick.Layouts

// Sidebar with tabs
Rectangle {
    Layout.preferredWidth: 200
    Layout.fillHeight: true
    color: Colores.rojo_unrn

    // Vertical layout for tabs
    ColumnLayout {
        anchors.fill: parent
        spacing: 0

        // Tab buttons
        Repeater {
            model: ["Home", "Profile", "Settings", "Messages", "Notifications"]
            
            Button {
                text: modelData
                Layout.fillWidth: true
                Layout.preferredHeight: 50
                
                // Button styling
                background: Rectangle {
                    color: tabLoader.currentIndex === index 
                            ? "#e0e0e0" 
                            : "transparent"
                }

                // Tab selection logic
                onClicked: {
                    tabLoader.currentIndex = index
                }
            }
        }

        // Spacer to push tabs to the top
        Item {
            Layout.fillHeight: true
        }
    }
}

