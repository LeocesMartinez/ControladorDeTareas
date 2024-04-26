import { Component, OnDestroy, OnInit } from '@angular/core';
import { Subscription } from 'rxjs';
import { ApiService } from '../../api/api.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-crear-tareas',
  templateUrl: './crear-tareas.component.html',
  styleUrl: './crear-tareas.component.css'
})
export class CrearTareasComponent implements OnInit, OnDestroy {
  mensajeError = "";
  private suscripcionServicio?: Subscription;

  constructor(private apiService: ApiService, private router: Router) { }
  
  ngOnInit(): void {
    const usuarioLogueado = localStorage.getItem('usuario');
    console.log('Iniciando componente de CrearTarea', usuarioLogueado);
    if(!usuarioLogueado) {
      this.router.navigate(['/usuario']);
    } 
  }
  
  ngOnDestroy(): void {
    if (this.suscripcionServicio) {
      this.suscripcionServicio.unsubscribe();
    }
  }

  //Borrar este metodo cuando se tenga el submitForm, tambien borrar el boton del HTML
  /*crearTarea(){
    this.submitForm({valid: true})
  }*/
  

  submitForm(form: any) {
    this.mensajeError = "";
    console.log('enviando')
    if (form.valid) {

      /*const tarea = {
        titulo: 'tituloEjmplo', //form.value.AquiNombreEnElHTML, 
        descripcion: 'DescEjemp',//form.value.password,
        fechaVencimiento: '2024-04-26',
        prioridad: 'ALTA',
        creadorTarea: localStorage.getItem('usuario'), //no cambia
        usuario_asignado: '123'

        
      };*/

      const tarea = {
        titulo: form.value.titulo,
        descripcion: form.value.descripcion,
        fechaVencimiento: form.value.fechaVencimiento,
        prioridad: form.value.prioridad,
        creadorTarea: localStorage.getItem('usuario'),
        usuario_asignado: form.value.usuario_asignado
      };
      
      //Invocar el servicio
      console.log('Objeto para invocar el servicio', tarea)

      if (this.suscripcionServicio) {
        this.suscripcionServicio.unsubscribe();
      }

      this.suscripcionServicio = this.apiService.create('crear-tareas', tarea)
      .subscribe({
        next: (datos) => {
          // Manejar datos exitosos aquí
          this.mensajeError = "";
          console.log('Datos exitosos:', datos);
          this.router.navigate(['/tareas']);

        },
        error: (error) => {
          // Manejar errores aquí
          this.mensajeError = "Ha ocurrido un error al crear la tarea";
          console.error('Error al obtener datos:', error);
        },
        complete: () => {
          // Manejar la finalización aquí si es necesario
        }
      });

    } else {
      this.mensajeError = "Debe llenar todos los campos del formulario";
      console.log('El formulario no es válido');
    }
  }

}
