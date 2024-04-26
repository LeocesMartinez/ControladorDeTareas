import { RouterModule, Routes } from "@angular/router";
import { TareasComponent } from "./tareas/tareas.component";
import { NgModule } from "@angular/core";
import { CrearTareasComponent } from "./crear-tareas/crear-tareas.component";
import { MostarTareasComponent } from "./mostar-tareas/mostar-tareas.component";
import { EliminarTareaComponent } from "./eliminar-tarea/eliminar-tarea.component";

const routes: Routes = [
    // new add eliminar-tarea component
    {path: '', component: TareasComponent} , 
    {path: 'crear', component: CrearTareasComponent },
    {path: 'ver', component: MostarTareasComponent },
    {path:'eliminar', component:EliminarTareaComponent}


  
 ];

@NgModule({
 imports: [RouterModule.forChild(routes)],
 exports: [RouterModule]
})
export class TasksRoutingModule { }