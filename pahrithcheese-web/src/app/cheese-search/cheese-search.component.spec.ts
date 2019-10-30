import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { CheeseSearchComponent } from './cheese-search.component';

describe('CheeseSearchComponent', () => {
  let component: CheeseSearchComponent;
  let fixture: ComponentFixture<CheeseSearchComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ CheeseSearchComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(CheeseSearchComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
