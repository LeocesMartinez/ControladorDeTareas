import { Component, OnDestroy, OnInit } from '@angular/core';
import { Subscription } from 'rxjs';
import { ApiService } from '../../api/api.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-eliminar-tarea',
  templateUrl: './eliminar-tarea.component.html',
  styleUrls: ['./eliminar-tarea.component.css']
})
export class EliminarTareaComponent implements OnInit, OnDestroy {
  mensajeError = "";
  private suscripcionServicio?: Subscription;

  constructor(private apiService: ApiService, private router: Router) { }
  
  ngOnInit(): void {
    const usuarioLogueado = localStorage.getItem('usuario');
    console.log('Iniciando componente de EliminarTarea', usuarioLogueado);
    if(!usuarioLogueado) {
      this.router.navigate(['/usuario']);
    } 
  }
  
  ngOnDestroy(): void {
    if (this.suscripcionServicio) {
      this.suscripcionServicio.unsubscribe();
    }
  }

  submitForm(form: any) {
    this.mensajeError = "";
    console.log('enviando')
    if (form.valid) {

      // Obtener ID de la tarea a eliminar
      const tareaId = form.value.tareaId;
      
      //Invocar el servicio para eliminar la tarea por su ID
      console.log('ID de tarea a eliminar:', tareaId);

      if (this.suscripcionServicio) {
        this.suscripcionServicio.unsubscribe();
      }

      this.suscripcionServicio = this.apiService.delete(`eliminar-tareas/${tareaId}`, null)
      .subscribe({
        next: (datos) => {
          // Manejar datos exitosos aquí
          this.mensajeError = "";
          console.log('Datos exitosos:', datos);
          this.router.navigate(['/tareas']);

        },
        error: (error) => {
          // Manejar errores aquí
          this.mensajeError = "Ha ocurrido un error al eliminar la tarea";
          console.error('Error al eliminar la tarea:', error);
        },
        complete: () => {
          // Manejar la finalización aquí si es necesario
        }
      });

    } else {
      this.mensajeError = "Debe proporcionar el ID de la tarea a eliminar";
      console.log('El formulario no es válido');
    }
  }
}
