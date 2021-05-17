using System;
public interface Observer
{
   void Update(object subject);
}


using System;
using System.Collections;
public abstract class Subject
{
   private ArrayList observers = new ArrayList(); 
   public void AddObserver(Observer observer)
   {
      observers.Add(observer);
   }
   public void RemoveObserver(Observer observer)
   {
      observers.Remove(observer);
   }
   public void Notify()
   {
      foreach(Observer observer in observers)
      {
         observer.Update(this);
      }
   }
}


using System;
public class Album : Subject
{
   private String name; 
   public Album(String name)
   { this.name = name; }   
   public void Play() 
   {
      Notify();
   }
   public String Name
   {
      get { return name; }
   }
}


using System;
public class BillingService : Observer
{
   public void Update(object subject)
   {
      if(subject is Album)
         GenerateCharge((Album)subject);
   }

   private void GenerateCharge(Album album) 
   {
      string name = album.Name;
   }
}

using System;

class Client
{
   [STAThread]
   static void Main(string[] args)
   {
      BillingService billing = new BillingService();
      Album album = new Album("Up");

      album.AddObserver(billing);

      album.Play();
   }
}