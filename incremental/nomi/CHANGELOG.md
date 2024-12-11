<h1 align="center"><a href="https://github.com/Nomi-CEu/Nomi-CEu/releases/tag/1.7.3"><img src="https://raw.githubusercontent.com/Nomi-CEu/Branding/main/Nomi%20CEu/Releases/1.7.3/1.7.3.png" alt="Release 1.7.3"></a></h1>

<p align="center"><em><b>More Bug Fixes, Some Polishing and Quest Book Improvements!</em></b></p>

<p align="center"><em>Featuring Drawer Emptying Fix and Engine Core Recipe Changes!</em></p>

<hr>

## Warning

**Please DO NOT revert any saves that have been loaded in this release to 1.7-beta-5c, 1.6.1b, 1.6.1a, or prior!**

<hr>

**Recipe Changelog** is available [here](https://github.com/Nomi-CEu/Branding/blob/main/Nomi%20CEu/Releases/1.7.3/Recipes%20Changed%20Since%201.7.2.md).

<hr>

# Changes Since 1.7.2

## Balancing Changes:
### Both Modes:
* Move Engine Cores to Fluid Canner ([#1060](https://github.com/Nomi-CEu/Nomi-CEu/pull/1060)) - @ghzdude ([`58d83ae`](https://github.com/Nomi-CEu/Nomi-CEu/commit/58d83ae427fe6776a8b7d411ad5bc1973588303f))
  * Allows for Easier Parallelisation and Mass Automation of Engine Cores
* Improve Circuit Etcher Recipe (Lazy AE2 Compat) ([#1058](https://github.com/Nomi-CEu/Nomi-CEu/pull/1058)) - @IntegerLimit ([`675c0b9`](https://github.com/Nomi-CEu/Nomi-CEu/commit/675c0b90219de96729e1c44d9b21c5e8843ca52b))
  * Now uses an Advanced Inscriber instead of an Inscriber

## Feature Additions:
### Both Modes:
* Add Tiny Coke ([#1079](https://github.com/Nomi-CEu/Nomi-CEu/pull/1079)) - @IntegerLimit ([`d429e33`](https://github.com/Nomi-CEu/Nomi-CEu/commit/d429e33a21f8381d01b2be791d9b2d056df975d9))
* Make Double Check on Terminal Default False ([#1078](https://github.com/Nomi-CEu/Nomi-CEu/pull/1078)) - @IntegerLimit ([`6bbb809`](https://github.com/Nomi-CEu/Nomi-CEu/commit/6bbb809e8269371d70aa1d859728d5c95685ab8d))
* Hide Higher Tier Muffler Hatches ([#1065](https://github.com/Nomi-CEu/Nomi-CEu/pull/1065)) - @IntegerLimit ([`e5f3697`](https://github.com/Nomi-CEu/Nomi-CEu/commit/e5f36974dd0f4625ad670419b1f828b8e762363a))
  * Higher Tier Muffler Hatches have No Uses, Especially Since Ashes Cannot be Extracted via Automation
  * Existing Higher Tier Hatches Will Not Disappear, Recycling Recipes for Them Still Exist
* Remove No-Loot Lost Cities Buildings and Chests ([#1062](https://github.com/Nomi-CEu/Nomi-CEu/pull/1062)) - @IntegerLimit ([`9ebec9e`](https://github.com/Nomi-CEu/Nomi-CEu/commit/9ebec9ee50792fdecac287ade7d3db7374ab0089))
* Add the FindMyItemsAndFluids Mod ([#1067](https://github.com/Nomi-CEu/Nomi-CEu/pull/1067)) - @IntegerLimit ([`19d75b2`](https://github.com/Nomi-CEu/Nomi-CEu/commit/19d75b2144eb6bd88451ed90c40bc3e7bfedf77a))
  * Improves Storage Management Early Game!
* Add Tooltips Saying P2P Type ([#1066](https://github.com/Nomi-CEu/Nomi-CEu/pull/1066)) - @IntegerLimit ([`96256f3`](https://github.com/Nomi-CEu/Nomi-CEu/commit/96256f300564f9e5dc7d9e219d70373e33251232))
* Update Nomi-Labs to 0.10.0 ([#1064](https://github.com/Nomi-CEu/Nomi-CEu/pull/1064)) - @IntegerLimit ([`4c3337e`](https://github.com/Nomi-CEu/Nomi-CEu/commit/4c3337e4e8593623ffdaad6e77bbd581a883f589))
  * Improves Steam Boiler's TOP Display
  * Warns about Blocked Vents in Steam Machines' TOP Displays

## Quest Book Changes:
### Both Modes:
* Add Quest For FindMyItemsAndFluids ([#1074](https://github.com/Nomi-CEu/Nomi-CEu/pull/1074)) - @smallming675 ([`30af4d9`](https://github.com/Nomi-CEu/Nomi-CEu/commit/30af4d962a637f2d24816d3fac0d4cee1cc952d9))
* Misc Questbook Tweaks ([#1069](https://github.com/Nomi-CEu/Nomi-CEu/pull/1069)) - @smallming675 ([`db99902`](https://github.com/Nomi-CEu/Nomi-CEu/commit/db99902d7ed735cc39252bd1ddf33396dcda564a))
  * Includes Cleanup of Dependencies, Typos and Quest Lines!

### Hard Mode:
* Emphasise Steam Vent Mechanics ([#1068](https://github.com/Nomi-CEu/Nomi-CEu/pull/1068)) - @IntegerLimit ([`c988a5e`](https://github.com/Nomi-CEu/Nomi-CEu/commit/c988a5e04eeb33a80736807cff0a454e20655700))

## Bug Fixes:
### Both Modes:
* Update Nomi-Labs to 0.10.0 ([#1064](https://github.com/Nomi-CEu/Nomi-CEu/pull/1064)) - @IntegerLimit ([`4c3337e`](https://github.com/Nomi-CEu/Nomi-CEu/commit/4c3337e4e8593623ffdaad6e77bbd581a883f589))
  * Fixes Issues with AE2 Terminal Auto Focusing
  * Fixes Steam Boiler Issues with Certain Fuels
  * Fixes Localisation Issues with TOP Tooltips
* Fix Empty Locked Drawers Resetting on World Load ([#1061](https://github.com/Nomi-CEu/Nomi-CEu/pull/1061)) - @IntegerLimit ([`bc2c8da`](https://github.com/Nomi-CEu/Nomi-CEu/commit/bc2c8dae4c939aee7248b36a7cdf40bfbbb0c803))
* Fix Vibrant Jetpack Recipe ([#1055](https://github.com/Nomi-CEu/Nomi-CEu/pull/1055)) - @IntegerLimit ([`dc256c1`](https://github.com/Nomi-CEu/Nomi-CEu/commit/dc256c13aad2070bd617dd4ffc7744c81700ba30))

## General Changes:
### Mod Updates:
* Nomi Labs: *v0.9.5 ⇥ v0.10.2* - @IntegerLimit ([`d429e33`](https://github.com/Nomi-CEu/Nomi-CEu/commit/d429e33a21f8381d01b2be791d9b2d056df975d9), [`5446c56`](https://github.com/Nomi-CEu/Nomi-CEu/commit/5446c56a970d97dd333bf3755e0cd80292852915), [`4c3337e`](https://github.com/Nomi-CEu/Nomi-CEu/commit/4c3337e4e8593623ffdaad6e77bbd581a883f589), ...)

### Mod Additions:
* FindMyItemsAndFluids: *v1.0.0* - @IntegerLimit ([`19d75b2`](https://github.com/Nomi-CEu/Nomi-CEu/commit/19d75b2144eb6bd88451ed90c40bc3e7bfedf77a))


**Full Changelog**: [`1.7.2...1.7.3`](https://github.com/Nomi-CEu/Nomi-CEu/compare/1.7.2...1.7.3)
