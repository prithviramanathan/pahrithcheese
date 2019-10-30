import { TestBed } from '@angular/core/testing';

import { CheeseApiService } from './cheese-api.service';

describe('CheeseApiService', () => {
  beforeEach(() => TestBed.configureTestingModule({}));

  it('should be created', () => {
    const service: CheeseApiService = TestBed.get(CheeseApiService);
    expect(service).toBeTruthy();
  });
});
