
import QtQuick
import QtQuick.Controls
import QtQuick.Layouts

// El botón de una pestaña.
// TODO: Íconos
Button {
    required property string nombre
    id: self
    Layout.fillWidth: true
    Layout.preferredHeight: 68

    contentItem: Text {
        text: parent.nombre
        font.pointSize: 22
        color: "white"
        horizontalAlignment: Text.AlignHRight
        verticalAlignment: Text.AlignVCenter
    }
    
    background: Rectangle {
        color: sidebar.pestaña_actual === self.nombre
                ? Constantes.rojo_unrn_oscuro 
                : "transparent"
    }

    // Tab selection logic
    onClicked: {
        parent.parent.pestaña_actual = self.nombre
    }
}
