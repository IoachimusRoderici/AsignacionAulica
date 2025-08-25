import QtQuick

pragma Singleton

QtObject {
    readonly property color rojo_unrn: "#EB1C38"
    readonly property color rojo_unrn_oscuro: "#B70C0C"
    
    readonly property int ancho_de_la_barra: 250
    readonly property int altura_de_los_botones: 68

    readonly property string título_texto: "Asignación Áulica"
    readonly property int título_tamaño: 28

    property string logo_unrn_path: assets_path + "/logo_unrn_blanco.svg"
    readonly property int logo_unrn_margen: 20
}
