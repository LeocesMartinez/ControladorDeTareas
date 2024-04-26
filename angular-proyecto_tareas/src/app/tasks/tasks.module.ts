import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { TasksRoutingModule } from './tasks-routing.module';
import { FormsModule } from '@angular/forms';
import { TareasComponent } from './tareas/tareas.component';
import { CrearTareasComponent } from './crear-tareas/crear-tareas.component';
import { ApiService } from '../api/api.service';
import { HttpClientModule } from '@angular/common/http';
import { MostarTareasComponent } from './mostar-tareas/mostar-tareas.component';
import { EliminarTareaComponent } from './eliminar-tarea/eliminar-tarea.component';


// new add eliminarcomponente
@NgModule({
  declarations: [TareasComponent, CrearTareasComponent, MostarTareasComponent, EliminarTareaComponent],
  imports: [
    CommonModule,
    TasksRoutingModule,
    FormsModule,
    HttpClientModule
  ],
  exports: [TareasComponent, CrearTareasComponent, MostarTareasComponent, EliminarTareaComponent],
  providers: [ApiService]
})
export class TasksModule { }
