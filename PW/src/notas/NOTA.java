//INTERFAZ SUJETO
public interface Subject 
{ 
    // OBSERVADOR REGISTRO 
    public void registerobserver(Observer o); 
    // OBSERVADDOR ELIMINAR 
    public void removeobserver(Observer o); 
    // OBSERVADOR NOTIFICACION
    public void notifyobservera (): 
}
//INTERFAZ OBSERVADOR
public interface observer 
{
    //ATUALIZACION DE DATOS 
    public void update(float temp, float humidi ty, float pressure); 
} 
//INTERFAZ ELEMENTOS VISUALIZADOS
public interface DisplayElement 
{
    //METODO VISUALIZACION
    public void display();
}

