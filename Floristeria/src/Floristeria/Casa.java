package Floristeria;

public class Casa {
	//atributos de clase
    //Atributos de clase
    private String color;
    private int numHabitaciones;
    private int numBanos;
    private boolean tienePatio;
    private boolean tieneParqueadero;
    
    /**
     * Constructor de la calse casa
     * @param color color de la casa
     * @param numHabitaciones # de habitaciones de la casa
     * @param numBanos # de baños de la casa
     * @param tienePatio coloque true o false dependiendo si hay o no patio 
     * @param tieneParqueadero coloque true o false si tiene parqueadero o no 
     */
    public Casa(String color, int numHabitaciones, int numBanos, boolean tienePatio, boolean tieneParqueadero) {
        this.color=color;
        this.numHabitaciones=numHabitaciones;
        this.numBanos=numBanos;
        this.tienePatio=tienePatio;
        this.tieneParqueadero=tieneParqueadero;    
    }
    public String describir() {
        String descripcion="La casa es de color " + this.color + ".Tiene" + this.numHabitaciones + " habitación(es) y " + this.numBanos + " baño(s).";
        if (tienePatio) {descripcion+="\nTiene Patio.";}
        if (tieneParqueadero) {descripcion+="\nTiene parqueadero.";}
        return descripcion;
    }
    public void pintar(String nuevoColor) {
        this.color=nuevoColor;
        System.out.println("La casa ha sido pintada de color "+ this.color);
    }
}