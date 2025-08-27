
import QtQuick
import QtQuick.Controls
import QtQuick.VectorImage
import QtQuick.Layouts

// El botón de una pestaña.
// TODO: Íconos
Button {
    required property string nombre
    id: self
    Layout.fillWidth: true
    Layout.preferredHeight: Constantes.pestaña_altura
    spacing: 0

    contentItem: Text {
        text: parent.nombre
        font.pointSize: Constantes.pestaña_texto_altura
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
