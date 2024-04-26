import { Component, OnDestroy, OnInit } from '@angular/core';
import { Subscription } from 'rxjs';
import { ApiService } from '../../api/api.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-mostar-tareas',
  templateUrl: './mostar-tareas.component.html',
  styleUrl: './mostar-tareas.component.css'
})
export class MostarTareasComponent implements OnInit, OnDestroy {
  mensajeError = "";
  tareas: any[] = [];
  estado: string = 'PENDIENTE';
  private suscripcionServicio?: Subscription;

  constructor(private apiService: ApiService, private router: Router) { }
  
  ngOnInit(): void {
    const usuarioLogueado = localStorage.getItem('usuario');
    console.log('Iniciando componente de MostrarTarea', usuarioLogueado);
    if(!usuarioLogueado) {
      this.router.navigate(['/usuario']);
    }

    this.verTareas();

  }

  verTareas() {
    if (this.suscripcionServicio) {
      this.suscripcionServicio.unsubscribe();
    }

    const paramsTareas = {
      usuarioAsignado: localStorage.getItem('usuario'),
      estado: this.estado
    };

    this.suscripcionServicio = this.apiService.getAll('mostrar-tareas', paramsTareas)
    .subscribe({
      next: (datos) => {
        // Manejar datos exitosos aquí
        this.mensajeError = "";
        this.tareas = datos;
        console.log('Datos exitosos:', datos);

      },
      error: (error) => {
        // Manejar errores aquí
        this.mensajeError = "Ha ocurrido un error al cargar las tareas";
        console.error('Error al obtener datos:', error);
      },
      complete: () => {
        // Manejar la finalización aquí si es necesario
      }
    });

  }

  eliminarTarea(tareaId: string) {
    if (this.suscripcionServicio) {
      this.suscripcionServicio.unsubscribe();
    }

    const paramsTareas = {
      tareaId: tareaId
    };

    this.suscripcionServicio = this.apiService.delete('eliminar-tarea', paramsTareas)
    .subscribe({
      next: (datos) => {
        // Manejar datos exitosos aquí
        this.mensajeError = "";
        console.log('Datos exitosos:', datos);
        this.verTareas();
      },
      error: (error) => {
        // Manejar errores aquí
        this.mensajeError = "Ha ocurrido un error al eliminar la tarea";
        console.error('Error al obtener datos:', error);
      },
      complete: () => {
        // Manejar la finalización aquí si es necesario
      }
    });
  }

  completarTarea(tareaId: string) {
    if (this.suscripcionServicio) {
      this.suscripcionServicio.unsubscribe();
    }

    const paramsTareas = {
      tareaId: tareaId,
      usuarioModificador: localStorage.getItem('usuario')
    };

    this.suscripcionServicio = this.apiService.update('marcarTareaCompletada', paramsTareas)
    .subscribe({
      next: (datos) => {
        // Manejar datos exitosos aquí
        this.mensajeError = "";
        console.log('Datos exitosos:', datos);
        this.verTareas();
      },
      error: (error) => {
        // Manejar errores aquí
        this.mensajeError = "Ha ocurrido un error al actualizar la tarea";
        console.error('Error al obtener datos:', error);
      },
      complete: () => {
        // Manejar la finalización aquí si es necesario
      }
    });
  }
  
  ngOnDestroy(): void {
    if (this.suscripcionServicio) {
      this.suscripcionServicio.unsubscribe();
    }
  }
}
