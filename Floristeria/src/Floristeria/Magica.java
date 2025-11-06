
package Floristeria;

public class Magica extends Casa {
    private String nombre;
    private int cantidadFlores;

    public Rossbella(String color, int numHabitaciones, int numBanos, boolean tienePatio, boolean tieneParqueadero,
                     String nombre, int cantidadFlores) {
        super(color, numHabitaciones, numBanos, tienePatio, tieneParqueadero);
        this.nombre = nombre;
        this.cantidadFlores = cantidadFlores;
    }

    public String describirFloristeria() {
        return super.describir() + " La floristería se llama " + nombre +
               " y tiene " + cantidadFlores + " flores disponibles.";
    }

    public void pintar(String nuevoColor) {
        System.out.println("Pintando la floristería con color: " + nuevoColor);
    }
}
