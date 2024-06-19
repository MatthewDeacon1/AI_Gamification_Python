import json
import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QGridLayout, QVBoxLayout, QScrollArea, QFrame
from PyQt6.QtGui import QPixmap, QFont
from PyQt6.QtCore import Qt
from Elmer.Daniel_JSON_Files_Elmer.badge_system.badge_verification import load_badges


insignias_app = load_badges()

class BadgeWidget(QFrame):
    def __init__(self, badge):
        super().__init__()

        self.setStyleSheet("""
            QFrame {
                border: 2px solid #3498db;
                border-radius: 10px;
                padding: 10px;
                background-color: #ecf0f1;
            }
            QLabel {
                font-family: 'Lato';
            }
        """)

        layout = QVBoxLayout()
        self.setLayout(layout)

        # Añadir la imagen de la insignia
        image_label = QLabel(self)
        pixmap = QPixmap("Elmer/Daniel_JSON_Files_Elmer/badge_system/medal_icon.png")
        image_label.setPixmap(pixmap)
        image_label.setScaledContents(True)
        image_label.setFixedSize(100, 100)
        image_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Añadir el título y la descripción en un solo QLabel
        title_desc_label = QLabel(f"<b>{badge['badge_title']}</b><br>{badge['badge_description']}", self)
        title_desc_label.setFont(QFont('Lato', 14))
        title_desc_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title_desc_label.setWordWrap(True)

        # Añadir los elementos al layout
        layout.addWidget(image_label)
        layout.addWidget(title_desc_label)

class VitrinaInsignias(QWidget):
    def __init__(self, nombre_usuario):      
        super().__init__()
        self.insignias = self.load_badges_per_user(nombre_usuario)
        self.initUI()

    def load_badges_per_user(self, nombre_usuario):
        # Cargar todas las insignias disponibles
        all_badges = insignias_app
        
        #insignias ganadas por el usuario
        user_badges_file = f"Elmer\\Daniel_JSON_Files_Elmer\\badge_progress\\{nombre_usuario}_badge_progress.json"
        with open(user_badges_file, "r", encoding='UTF-8') as file:
            user_badges = json.load(file)
        
        # Filtrar las insignias
        earned_badges = []
        for badge in all_badges:
            badge_id = badge['badge_id']
            if badge_id in user_badges and user_badges[badge_id]:
                earned_badges.append(badge)
        return earned_badges

    def initUI(self):
        # Configuración de la ventana principal
        self.setWindowTitle('Vitrina de Insignias')
        self.setGeometry(100, 100, 800, 600)

        # Crear el área de desplazamiento
        scroll_area = QScrollArea(self)
        scroll_area.setWidgetResizable(True)

        # Crear un widget contenedor para el área de desplazamiento
        container_widget = QWidget()
        scroll_area.setWidget(container_widget)

        # Layout principal
        layout = QVBoxLayout(container_widget)
        container_widget.setLayout(layout)

        # Layout de la cuadrícula de insignias
        grid_layout = QGridLayout()
        grid_layout.setSpacing(10)

        # Añadir insignias al layout
        row, col = 0, 0
        for i, insignia in enumerate(self.insignias):
            badge_widget = BadgeWidget(insignia)
            grid_layout.addWidget(badge_widget, row, col)

            col += 1
            if col >= 3:  # Cambiar esta cifra para ajustar el número de columnas
                col = 0
                row += 1

        # Añadir el grid layout al layout principal
        layout.addLayout(grid_layout)

        # Layout principal del widget
        main_layout = QVBoxLayout(self)
        main_layout.addWidget(scroll_area)
        self.setLayout(main_layout)

def main():
    app = QApplication(sys.argv)
    ex = VitrinaInsignias("Prisila")
    ex.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()
