import { ComponentFixture, TestBed } from '@angular/core/testing';

import { MostarTareasComponent } from './mostar-tareas.component';

describe('MostarTareasComponent', () => {
  let component: MostarTareasComponent;
  let fixture: ComponentFixture<MostarTareasComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [MostarTareasComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(MostarTareasComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
