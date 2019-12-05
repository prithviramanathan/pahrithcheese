import { Component, OnInit } from '@angular/core';
import { CheeseApiService } from '../services/cheese-api.service';
import { ToastrService } from 'ngx-toastr';

export interface Store {
  storeAddress: string;
  storeName: string;
}
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
  locations: [Store];
}

@Component({
  selector: 'app-cheese-search',
  templateUrl: './cheese-search.component.html',
  styleUrls: ['./cheese-search.component.scss']
})
export class CheeseSearchComponent implements OnInit {
  cheeseData: Cheese;

  constructor(private cheeseService: CheeseApiService, private toastrService: ToastrService) { 
  }

  ngOnInit() {
  }

  populateFields(cheese: string) {
    this.cheeseService.getCheese(cheese).subscribe((data)=>{
      this.cheeseData = data[0];
    });
  }

  addPairing(cheese: string, pairing: string) {
    console.log(cheese, pairing);
    this.cheeseService.updatePairing(cheese, pairing).subscribe((data) => {
      this.toastrService.success('Updated pairing!');
    });
  }

  addToFavorites() {
    this.cheeseService.toggleLike(this.cheeseService.getEmail(), this.cheeseData.name).subscribe((data) => {
      console.log(data);
      if(data[0] === 'removed like') {
        this.toastrService.warning('Unfavorited the cheese!');
      }
      else if (data[0] === 'liked the cheese') {
        this.toastrService.success('Favorited the cheese!');
      }
    });
  }

}
