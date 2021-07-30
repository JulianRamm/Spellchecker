import { HttpClientModule } from '@angular/common/http';
import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { MatCardModule } from '@angular/material/card';
import { MatButtonModule } from '@angular/material/button';
import { MatInputModule } from '@angular/material/input';
import { MatProgressBarModule } from '@angular/material/progress-bar';
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { SpellcheckerService } from './spellchecker.service';
import { SpellcheckerComponent } from './spellchecker/spellchecker.component';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { NgbModule } from '@ng-bootstrap/ng-bootstrap';
import {FormsModule, ReactiveFormsModule} from '@angular/forms';

@NgModule({
  declarations: [
    AppComponent,
    SpellcheckerComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule,
    BrowserAnimationsModule,
    MatCardModule,
    MatButtonModule,
    MatInputModule,
    NgbModule,
    FormsModule,
    MatProgressBarModule,
    ReactiveFormsModule
  ],
  providers: [SpellcheckerService],
  bootstrap: [AppComponent]
})
export class AppModule { }
