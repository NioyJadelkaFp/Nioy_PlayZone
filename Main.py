from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def inedx():
    titulos:str = 'Home'

    # Conectar a la base de datos SQLite
    conn = sqlite3.connect('backend/juegos.db')
    cursor = conn.cursor()
    
    # Ejecutar consulta para obtener todos los juegos
    cursor.execute("SELECT id, nombre, desarrolladora, categoria, año, links_android, link_pc, link_img FROM juegos")
    
    # Obtener todos los resultados
    juegos = cursor.fetchall()
    
    # Cerrar la conexión a la base de datos
    conn.close()

    return render_template('index.html', titulos=titulos, juegos=juegos)

@app.route('/terror')
def terror():
    titulos: str = 'Juegos de Terror'

    # Conectar a la base de datos SQLite
    conn = sqlite3.connect('backend/juegos.db')
    cursor = conn.cursor()
    
    # Ejecutar consulta para obtener solo los juegos de la categoría 'Terror'
    cursor.execute("SELECT id, nombre, desarrolladora, categoria, año, links_android, link_pc, link_img FROM juegos WHERE categoria = 'Horror'")
    
    # Obtener todos los resultados
    juegos_terror = cursor.fetchall()
    
    # Cerrar la conexión a la base de datos
    conn.close()

    return render_template('terror.html', titulos=titulos, juegos=juegos_terror)

@app.route('/diversion')
def diversion():
    titulos: str = 'Juegos de Diversión'

    # Conectar a la base de datos SQLite
    conn = sqlite3.connect('backend/juegos.db')
    cursor = conn.cursor()
    
    # Ejecutar consulta para obtener solo los juegos de la categoría 'Diversión'
    cursor.execute("SELECT id, nombre, desarrolladora, categoria, año, links_android, link_pc, link_img FROM juegos WHERE desarrolladora = 'Gameloft'")
    
    # Obtener todos los resultados
    juegos_diversion = cursor.fetchall()
    
    # Cerrar la conexión a la base de datos
    conn.close()

    return render_template('diversion.html', titulos=titulos, juegos=juegos_diversion)



if __name__ == '__main__':
    app.run(debug=True)