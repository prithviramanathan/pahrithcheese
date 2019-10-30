import { Component, OnInit } from '@angular/core';
import { CheeseApiService } from '../services/cheese-api.service';

@Component({
  selector: 'app-cheese-search',
  templateUrl: './cheese-search.component.html',
  styleUrls: ['./cheese-search.component.scss']
})
export class CheeseSearchComponent implements OnInit {

  constructor(private cheeseService: CheeseApiService) { }

  ngOnInit() {
  }

}
