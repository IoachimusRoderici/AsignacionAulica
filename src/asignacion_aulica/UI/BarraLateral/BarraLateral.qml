import QtQuick
import QtQuick.Window
import QtQuick.Controls
import QtQuick.Layouts

// Sidebar with tabs
Rectangle {
    Layout.preferredWidth: 250
    Layout.fillHeight: true
    color: Colores.rojo_unrn

    // Vertical layout for tabs
    ColumnLayout {
        anchors.fill: parent
        spacing: 0

        // Tab buttons
        Repeater {
            model: ["Home", "Profile", "Settings", "Messages", "Notifications"]
            
            BotónPestaña{
                text: modelData
            }
        }

        // Spacer to push tabs to the top
        Item {
            Layout.fillHeight: true
        }
    }
}

