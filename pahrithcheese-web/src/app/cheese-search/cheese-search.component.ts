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
    this.cheeseData = {"country_of_origin": "Italy", "pairing": "", "fat_content": "25.83  g/100g", "name": "Parmesan", "family": "Parmesan", "region": "Provinces of Parma, Reggio Emilia, Modena, Bologna , Mantua", "texture": "crystalline, dense and grainy", "aroma": "strong", "image": "https://www.cheese.com/media/img/cheese/Parmesan_1.jpg", "flavor": "fruity, nutty, savory, sharp", "type": "hard, artisan", "color": "straw", "description": "The Parmigiano Reggiano or Parmesan cheese as it is called in English is considered to be among the top cheeses by cheese connoisseurs. Today, it is produced by various producers. However, PDO designation states that for a cheese to be called as Parmesan, it has to be produced from cows grazing on fresh grass and hay.\r\nCheeses mocking Parmigiano Reggiano are called as Parmesan or Italian hard cheese by producers to avoid legal issues.&amp;nbsp;Parmigiano Reggiano cheese is named after the provinces in which it is made, namely Provinces of Parma, Reggio Emilia, Modena, Bologna and Mantua.\r\nTrue Parmesan cheese has a hard, gritty texture and is fruity and nutty in taste. Cheeses mocking Parmesan or inferior Parmesan may have a bitter taste. Parmigiano Reggiano cheese is mostly grated over pastas, used in soups and risottos. It is also eaten on its own as a snack."};
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
