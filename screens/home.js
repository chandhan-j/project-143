import React, { Component } from "react";
import { View, Text, StyleSheet, Image, TouchableOpacity } from "react-native";
import { Header, AirbnbRating, Icon } from "react-native-elements";
import { RFValue } from "react-native-responsive-fontsize";
import axios from "axios";
import { SafeAreaView } from "react-native-safe-area-context";

export default class HomeScreen extends Component {
  constructor() {
    super();
    this.state = {
      articleDetails: {}
    };
  }

  componentDidMount() {
    this.getArticles();
  }

  getArticles = () => {
    const url = "https://a628-74-111-101-198.ngrok.io";
    axios
      .get(url)
      .catch(error => {
        console.log(error.message);
      });
  };

  likedArticle = () => {
    const url = "https://a628-74-111-101-198.ngrok.io/liked-article";
    axios
      .post(url)
      .catch(error => {
        console.log(error.message);
      });
  };

  unlikedArticle = () => {
    const url = "https://a628-74-111-101-198.ngrok.io/unliked-article";
    axios
      .post(url)
      .catch(error => {
        console.log(error.message);
      });
  };

  notWatched = () => {
    const url = "https://a628-74-111-101-198.ngrok.io/did-not-watch";
    axios
      .post(url)
      .catch(error => {
        console.log(error.message);
      });
  };
  render()
  {
    return(
      <Text>Home Screen</Text>
    )
  }
}
