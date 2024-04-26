import { Component, OnDestroy, OnInit } from '@angular/core';
import { ApiService } from '../../api/api.service';
import { Subject, Subscription, takeUntil } from 'rxjs';
import { Router } from '@angular/router';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrl: './login.component.css'
})
export class LoginComponent implements OnInit, OnDestroy {
  mensajeError = "";
  private suscripcionServicio?: Subscription;

  constructor(private apiService: ApiService, private router: Router) { }
  
  ngOnInit(): void {
    console.log('Iniciando componente de Login')
    const usuarioLogueado = localStorage.getItem('usuario');
    if(usuarioLogueado) {
      this.router.navigate(['/tareas']);
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

      const login = {
        username: form.value.usuario, 
        password: form.value.password
      };
      //Invocar el servicio
      console.log('Objeto para invocar el servicio', login)

      if (this.suscripcionServicio) {
        this.suscripcionServicio.unsubscribe();
      }

      this.suscripcionServicio = this.apiService.create('login-usuario', login)
      .subscribe({
        next: (datos) => {
          // Manejar datos exitosos aquí
          this.mensajeError = "";
          console.log('Datos exitosos:', datos);
          localStorage.setItem('usuario', login.username);
          this.router.navigate(['/tareas']);
          //this.reloadPage();

        },
        error: (error) => {
          // Manejar errores aquí
          this.mensajeError = "Ha ocurrido un error en el login del usuario: usuario y/o constraseña incorrecta.";
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

  reloadPage() {
    this.router.navigateByUrl('/', { skipLocationChange: true }).then(() => {
      this.router.navigate([this.router.url]);
    });
  }
}
