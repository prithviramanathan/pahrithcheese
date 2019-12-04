import { Component, OnInit } from '@angular/core';
import { CheeseApiService } from '../services/cheese-api.service';

export interface Cheese {
  country_of_origin: string;
  fat_content: string;
  name: string;
  family: string;
  color: string;
  region: string;
  pairing: string;
  texture: string;
  aroma: string;
  flavor: string;
  type: string;
  image: string;
  description: string;
}

@Component({
  selector: 'app-cheese-search',
  templateUrl: './cheese-search.component.html',
  styleUrls: ['./cheese-search.component.scss']
})
export class CheeseSearchComponent implements OnInit {
  cheeseData: Cheese;

  constructor(private cheeseService: CheeseApiService) { }

  ngOnInit() {
  }

  populateFields(cheese: string) {
    this.cheeseService.getCheese(cheese).subscribe((data)=>{
      this.cheeseData = data[0];
    });
  }

  addPairing(cheese: string, pairing: string) {
    this.cheeseService.updatePairing(cheese, pairing).subscribe((data) => {
      console.log(data);
    });
  }

}