import QtQuick
import QtQuick.Window
import QtQuick.Controls
import QtQuick.Layouts

Rectangle {
    Layout.preferredWidth: 250
    Layout.fillHeight: true
    color: Colores.rojo_unrn

    ColumnLayout {
        anchors.fill: parent
        spacing: 0

        // Botones de las pestañas
        BotónPestaña{ text: "Edificios" }
        BotónPestaña{ text: "Aulas"     }
        BotónPestaña{ text: "Carreras"  }
        BotónPestaña{ text: "Materias"  }
        BotónPestaña{ text: "Horarios"  }

        // Spacer to push tabs to the top
        Item {
            Layout.fillHeight: true
        }
    }
}

