import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { LoginComponent } from './login/login.component';
import { RegistroComponent } from './registro/registro.component';
import { UsuarioRoutingModule } from './usuario-routing.module';
import { FormsModule } from '@angular/forms';
import { ApiService } from '../api/api.service';
import { HttpClientModule } from '@angular/common/http';

@NgModule({
  declarations: [LoginComponent,RegistroComponent],
  imports: [
    CommonModule,
    UsuarioRoutingModule,
    FormsModule,
    HttpClientModule
  ], 
  exports: [LoginComponent,RegistroComponent],
  providers: [ApiService]
})
export class UsuarioModule { }
