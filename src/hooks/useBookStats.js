import { useContext, useMemo } from "react";
import { BookContext } from "../context/BookContext";

const useBookStats = () => {
  const { books } = useContext(BookContext);

  const stats = useMemo(() => {
    const total = books.length;
    const owned = books.filter((b) => b.status === "owned").length;
    const reading = books.filter((b) => b.status === "reading").length;
    const wishlist = books.filter((b) => b.status === "wishlist").length;

    return { total, owned, reading, wishlist };
  }, [books]);

  return stats;
};

export default useBookStats;
