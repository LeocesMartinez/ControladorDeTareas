import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { LoginComponent } from './login/login.component';
import { RegistroComponent } from './registro/registro.component';
import { UsuarioRoutingModule } from './usuario-routing.module';



@NgModule({
  declarations: [LoginComponent,RegistroComponent],
  imports: [
    CommonModule,
    UsuarioRoutingModule
  ], exports: [LoginComponent,RegistroComponent]
})
export class UsuarioModule { }
