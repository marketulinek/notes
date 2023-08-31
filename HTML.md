# HTML

## Tables
### < colgroup >
Define the table columns and style them as desired (such as certain columns aligned or colored differently). Without this, individual cells would need to be targeted.

```
<table>
  <colgroup>
    <col class="first">
    <col class="second">
  </colgroup>
  <colgroup class="other">
    <col>
    <col>
  </colgroup>
  <tbody>
    <tr>
      <td>first</td>
      <td>second</td>
      <td>other</td>
      <td>other</td>
    </tr>
    <tr>
      <td>first</td>
      <td>second</td>
      <td>other</td>
      <td>other</td>
    </tr>
  </tbody>
</table>
```
### < caption >
```
<table>
    <caption>Locust mating habits</caption>
<!-- etc. -->
```
### < datalist >
Takes the form of a list of suggestions that accompanies a text field.
```
<input name="country" list="country_name">
<datalist id="country_name">
    <option value="Albania">
    <option value="Algeria">
    <option value="Andorra">
    ...
</datalist>
```
### < canvas >
Designed to provide a canvas onto which JavaScript can be used to paint images such as graphs, animated sprites, ...
```
<canvas id="myChart"></canvas>
```

## Images
- **JPEGs**
  - used for images such as photographs
  - the lower the compression, the higher the file size, but the clearer the image
- **GIFs**
  - used for images with solid colors (icons, logos)
  - can have no more than 256 colors
  - the lower the number of colors in the image, the lower the file size will be
  - allow any pixel to be transparent
- **PNGs**
  - used for versatile images in more complex designs
  - not fully supported by some older browsers
  - allows 16 million colors
