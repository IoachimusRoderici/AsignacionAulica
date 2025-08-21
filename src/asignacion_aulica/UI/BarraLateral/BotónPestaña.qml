
import QtQuick
import QtQuick.Controls
import QtQuick.Layouts

// El botón de una pestaña.
// Propiedad obligatoria: text (nombre de la pestaña)
// TODO: Íconos
Button {
    id: self
    Layout.fillWidth: true
    Layout.preferredHeight: 68
    font.pointSize: 20
    
    background: Rectangle {
        color: tabLoader.pestaña_actual === self.text
                ? Colores.pestaña_seleccionada 
                : "transparent"
    }

    // Tab selection logic
    onClicked: {
        tabLoader.pestaña_actual = self.text
    }
}
