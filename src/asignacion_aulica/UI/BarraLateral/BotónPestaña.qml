
import QtQuick
import QtQuick.Controls
import QtQuick.Layouts

// El botón de una pestaña.
// Propiedad obligatoria: text (nombre de la pestaña)
Button {
    Layout.fillWidth: true
    Layout.preferredHeight: 68
    
    // Button styling
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
