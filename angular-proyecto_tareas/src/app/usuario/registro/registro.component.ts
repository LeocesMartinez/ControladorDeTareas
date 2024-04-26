import { Component, OnDestroy, OnInit } from '@angular/core';
import { Subscription } from 'rxjs';
import { ApiService } from '../../api/api.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-registro',
  templateUrl: './registro.component.html',
  styleUrl: './registro.component.css'
})
export class RegistroComponent implements OnInit, OnDestroy {
  mensajeError = "";
  private suscripcionServicio?: Subscription;

  constructor(private apiService: ApiService, private router: Router) { }
  
  ngOnInit(): void {
    const usuarioLogueado = localStorage.getItem('usuario');
    console.log('Iniciando Componente registro: ', usuarioLogueado);
    /*if(usuarioLogueado) {
      this.router.navigate(['/tareas']);
    }*/ 
  }
  
  ngOnDestroy(): void {
    if (this.suscripcionServicio) {
      this.suscripcionServicio.unsubscribe();
    }
  }

  submitForm(form: any) {
    console.log('enviando')
    if (form.valid) {    

      const registro = {
        usuarioId: form.value.id_usuario, 
        nombre: form.value.nombre,
        apellido: form.value.apellido, 
        password: form.value.password
      };

      if (this.suscripcionServicio) {
        this.suscripcionServicio.unsubscribe();
      }

      this.suscripcionServicio = this.apiService.create('registrar-usuario', registro)
      .subscribe({
        next: (datos) => {
          // Manejar datos exitosos aquí
          this.mensajeError = "";
          console.log('Datos exitosos:', datos);
          this.router.navigate(['/usuario']);

        },
        error: (error) => {
          // Manejar errores aquí
          this.mensajeError = "Ha ocurrido un error en el registro de usuario del usuario.";
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
