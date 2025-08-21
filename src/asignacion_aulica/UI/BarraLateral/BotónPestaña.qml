
import QtQuick
import QtQuick.Controls
import QtQuick.Layouts

// El botón de una pestaña.
// Propiedad obligatoria: text (nombre de la pestaña)
// TODO: Íconos
Button {
    Layout.fillWidth: true
    Layout.preferredHeight: 68
    
    background: Rectangle {
        color: tabLoader.currentIndex === index 
                ? Colores.pestaña_seleccionada 
                : "transparent"
    }

    // Tab selection logic
    onClicked: {
        tabLoader.currentIndex = index
    }
}
