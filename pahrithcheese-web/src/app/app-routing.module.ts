import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { HomePageComponent } from './home-page/home-page.component';
import { CheeseSearchComponent } from './cheese-search/cheese-search.component';
import { UserComponent } from './user/user.component';


const routes: Routes = [{ path: 'home', component: HomePageComponent}, 
                        { path: 'search', component: CheeseSearchComponent},
                        { path: 'user', component: UserComponent},
                        { path: '**', redirectTo: '/home'}];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
