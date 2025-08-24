import QtQuick
import QtQuick.Window
import QtQuick.Controls
import QtQuick.Layouts

Rectangle {
    Layout.preferredWidth: Constantes.ancho_de_la_barra
    Layout.fillHeight: true
    color: Constantes.rojo_unrn

    property string pestaña_actual: "Edificios"

    ColumnLayout {
        anchors.fill: parent
        spacing: 0

        // Botones de las pestañas
        BotónPestaña{ nombre: "Edificios" }
        BotónPestaña{ nombre: "Aulas"     }
        BotónPestaña{ nombre: "Carreras"  }
        BotónPestaña{ nombre: "Materias"  }
        BotónPestaña{ nombre: "Horarios"  }

        // Spacer to push tabs to the top
        Item {
            Layout.fillHeight: true
        }

        Image {
            id: logoUNRN
            Layout.alignment: Qt.AlignBottom | Qt.AlignHCenter
            Layout.margins: Constantes.logo_unrn_margen
            Layout.fillWidth: true
            fillMode: Image.PreserveAspectFit
            source: Constantes.logo_unrn_path
        }
    }
}

